const problems = [];
document.querySelectorAll('a[href^="/problems/"][target="_blank"]').forEach(a => {
    const url = a.getAttribute('href').split('?')[0].replace(/\/$/, '');

    const titleDiv = a.querySelector('.ellipsis.line-clamp-1');
    const rawText = titleDiv ? titleDiv.textContent.trim() : null;

    const match = rawText && rawText.match(/^(\d+\.\s+\D+?)(?=\d|$)/);
    const title = match ? match[1].trim() : rawText;

    if (title && url && !problems.find(p => p.url === url)) {
        problems.push({url, title});
    }
});

console.log(JSON.stringify(problems, null, 2));
