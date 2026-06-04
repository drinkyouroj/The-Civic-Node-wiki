// IssueRow.jsx — single archive row, expandable lede

function IssueRow({ issue, expanded, onToggle, onOpen }) {
  return (
    <article className={"tcn-issue " + (expanded ? "is-expanded" : "")}>
      <div className="tcn-issue-meta">
        <span>DISPATCH №{String(issue.number).padStart(3, "0")}</span>
        <span aria-hidden>·</span>
        <span>{issue.date}</span>
        <span aria-hidden>·</span>
        <span>{issue.readingTime} MIN · {issue.words.toLocaleString()} WORDS</span>
      </div>

      <h2 className="tcn-issue-title">
        <a href={"#issue-" + issue.number}
           onClick={(e) => { e.preventDefault(); onOpen(issue); }}>{issue.title}</a>
      </h2>

      <p className="tcn-issue-dek">{issue.dek}</p>

      {expanded && (
        <p className="tcn-issue-lede">
          {issue.lede}
        </p>
      )}

      <div className="tcn-issue-foot">
        <div className="tcn-issue-tags">
          {issue.tags.map(t => <span key={t} className="tcn-issue-tag">{t}</span>)}
        </div>
        <button className="tcn-issue-toggle"
                onClick={() => onToggle(issue.number)}>
          {expanded ? "Collapse ←" : "Read lede →"}
        </button>
      </div>

      <hr className="tcn-hairline tcn-issue-rule" />
    </article>
  );
}

window.IssueRow = IssueRow;
