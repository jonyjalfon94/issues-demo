const issueBody = `${{ github.event.issue.body }}`;
const prUrls = issueBody.match(/(http|https):\/\/[a-zA-Z0-9./?=_%:-]*/g).sort()
console.log(prUrls);

prUrls.forEach(url => {
  console.log("PR URL: " + url);
  const prData = exec.exec('gh pr view ' + url + ' --json headRefName,headRepository');
  console.log(prData)
})