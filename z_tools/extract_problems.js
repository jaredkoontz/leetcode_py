const problems = [];
document.querySelectorAll('a[href^="/problems/"]').forEach(a => {
  let url = a.getAttribute('href').split('?')[0].replace(/\/$/, ''); // Strip query & trailing slash
  const rawText = a.textContent.trim();

  const match = rawText.match(/^(\d+\.\s+[^\d]+?)(?=\d|$)/);
  const title = match ? match[1].trim() : rawText;

  if (title && url && !problems.find(p => p.url === url)) {
    problems.push({ url, title });
  }
});
console.log(JSON.stringify(problems, null, 2));
