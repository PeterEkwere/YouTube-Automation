/* globals resolve, offsets */
'use strict';

const df = (new Date()).getTimezoneOffset();

const notify = message => chrome.notifications.create({
  type: 'basic',
  iconUrl: 'data/icons/48.png',
  title: chrome.runtime.getManifest().name,
  message
});

const randoms = {};
chrome.tabs.onRemoved.addListener(tabId => delete randoms[tabId]);

const onCommitted = ({ url, tabId, frameId }) => {
  if (url && url.startsWith('http')) {
    let location = localStorage.getItem('location');
    const standard = localStorage.getItem('standard');
    const daylight = localStorage.getItem('daylight');

    let offset = localStorage.getItem('offset') || 0;
    let msg = localStorage.getItem('isDST') === 'false' ? standard : daylight;

    if (localStorage.getItem('random') === 'true') {
      const ofs = Object.keys(offsets);
      if (frameId === 0 || randoms[tabId] === undefined) {
        location = ofs[Math.floor(Math.random() * ofs.length)];
        randoms[tabId] = location;
      }
      else {
        location = randoms[tabId];
      }
      const o = resolve.analyze(location);
      offset = o.offset;
      msg = offset !== o.offset ? o.storage.msg.daylight : o.storage.msg.standard;
    }
    chrome.tabs.executeScript(tabId, {
      runAt: 'document_start',
      frameId,
      matchAboutBlank: true,
      code: `document.documentElement.appendChild(Object.assign(document.createElement('script'), {
        textContent: 'Date.prefs = ["${location}", ${-1 * offset}, ${df}, "${msg}"];'
      })).remove();`
    }, () => chrome.runtime.lastError);
  }
};

const update = () => chrome.storage.local.get({
  enabled: true
}, ({ enabled }) => {
  if (enabled) {
    chrome.webNavigation.onCommitted.addListener(onCommitted);
  }
  else {
    chrome.webNavigation.onCommitted.removeListener(onCommitted);
  }
  chrome.browserAction.setIcon({
    path: {
      '16': 'data/icons' + (enabled ? '' : '/disabled') + '/16.png',
      '32': 'data/icons' + (enabled ? '' : '/disabled') + '/32.png',
      '48': 'data/icons' + (enabled ? '' : '/disabled') + '/48.png',
      '64': 'data/icons' + (enabled ? '' : '/disabled') + '/64.png'
    }
  });
  chrome.browserAction.setTitle({
    title: chrome.runtime.getManifest().name + ` (spoofing ${enabled ? 'enabled' : 'disabled'})`
  });
});
chrome.storage.onChanged.addListener(prefs => {
  if (prefs.enabled) {
    update();
  }
});
update();

const set = (timezone = 'Etc/GMT') => {
  const { offset, storage } = resolve.analyze(timezone);
  localStorage.setItem('offset', offset);
  localStorage.setItem('isDST', offset !== storage.offset);
  localStorage.setItem('location', timezone);
  localStorage.setItem('daylight', storage.msg.daylight);
  localStorage.setItem('standard', storage.msg.standard);
};

// browserAction
// chrome.browserAction.onClicked.addListener(() => chrome.storage.local.get({
//   enabled: true
// }, ({enabled}) => chrome.storage.local.set({
//   enabled: !enabled
// })));
chrome.browserAction.onClicked.addListener(() => {
  chrome.storage.local.set({
    enabled: true
  });
});

const server = async (silent = true) => {
  try {
    const timezone = await resolve.remote();

    if (localStorage.getItem('location') !== timezone) {
      set(timezone);
    }
    else if (silent === false) {
    }
  }
  catch (e) {
    if (silent === false) {
    }
    if (e.message.indexOf('JSON at position') !== -1) {
      setTimeout(server, 500, silent);
    }
  }
};

// on installed
chrome.runtime.onInstalled.addListener(() => {
  set(localStorage.getItem('location') || 'Etc/GMT');
});
// update on startup?
{
  const callback = () => {
      server();
  };
  chrome.runtime.onInstalled.addListener(callback);
  chrome.runtime.onStartup.addListener(callback);
}
// context menu
{
  const callback = () => {
    chrome.contextMenus.create({
      title: 'Check my current timezone',
      id: 'check-timezone',
      contexts: ['browser_action']
    });
    chrome.contextMenus.create({
      title: 'Update timezone from IP',
      id: 'update-timezone',
      contexts: ['browser_action']
    });
  };
  chrome.runtime.onInstalled.addListener(callback);
  chrome.runtime.onStartup.addListener(callback);
}

chrome.contextMenus.onClicked.addListener(({ menuItemId }) => {
  if (menuItemId === 'update-timezone') {
    server(false);
  }
  else if (menuItemId === 'check-timezone') {
    chrome.tabs.create({
      url: 'https://webbrowsertools.com/timezone/'
    });
  }
});
