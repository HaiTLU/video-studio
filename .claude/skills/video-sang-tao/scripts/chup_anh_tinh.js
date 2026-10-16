// Chụp ảnh tĩnh từ index.html của dự án video: node chup_anh_tinh.js <thư mục dự án> <thư mục ra> <giây> [giây...]
let pw; try { pw = require('playwright'); } catch (e) { pw = require('/opt/node22/lib/node_modules/playwright'); }
const { chromium } = pw;
const path = require('path');
(async () => {
  const proj = process.argv[2], out = process.argv[3], times = process.argv.slice(4).map(Number);
  const b = await chromium.launch({ executablePath: process.env.CHROME_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  p.on('console', m => console.log('console:', m.text())); p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + path.resolve(proj, 'index.html'));
  await p.evaluate(() => window.__ready);
  for (const t of times) {
    await p.evaluate(t => window.seek(t), t);
    await p.locator('#c').screenshot({ path: `${out}/t${t.toFixed(2)}.png` });
  }
  await b.close();
})();
