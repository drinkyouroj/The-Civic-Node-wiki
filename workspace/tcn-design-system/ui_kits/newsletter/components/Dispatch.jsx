// Dispatch.jsx — full reading view of one dispatch

function Disclosure() {
  return (
    <aside className="tcn-disclosure">
      <b>Standard disclosure</b>
      <p>
        No token positions, advisory roles, allocation letters, or sponsored content.
        If I have an operational relationship with a project or infrastructure mentioned
        in this piece, it is disclosed in the body before the relevant analysis. If I'm
        wrong, the primary sources are linked — you can check.
      </p>
    </aside>
  );
}

function Dispatch({ issue, onBack }) {
  return (
    <article className="tcn-dispatch">
      <button className="tcn-back" onClick={onBack}>← Back to archive</button>

      <div className="tcn-issue-meta">
        <span>DISPATCH №{String(issue.number).padStart(3, "0")}</span>
        <span aria-hidden>·</span>
        <span>{issue.date}</span>
        <span aria-hidden>·</span>
        <span>{issue.readingTime} MIN · {issue.words.toLocaleString()} WORDS</span>
      </div>

      <h1 className="tcn-dispatch-title">{issue.title}</h1>
      <p className="tcn-dispatch-dek">{issue.dek}</p>

      <hr className="tcn-hairline" />

      <div className="tcn-dispatch-body">
        <p className="tcn-lead">{issue.lede}</p>

        <h3>[01] Context</h3>
        <p>
          The Treasury has signalled it three times now. The first time it was a
          footnote in a refunding announcement; the second, an off-the-record
          backgrounder. This week it landed in a published auction calendar. Worth
          taking seriously.
        </p>

        <h3>[02] Frame</h3>
        <p>
          Three frames for thinking about the crowding-out paradox. The first two are
          the ones every analyst reaches for. The third is the one most people miss —
          and it's the only one that explains the last six months of yields.
        </p>
        <ol>
          <li><b>Stock-flow.</b> The Treasury sells, the market clears, the price moves. This works for cash in normal weeks. It does not work this week.</li>
          <li><b>Convexity.</b> Dealers absorb whatever stock-flow can't, but at a cost that compounds with duration. We've seen this before.</li>
          <li><b>Settlement.</b> The pipes themselves have capacity. When sovereign issuance crosses dealer balance-sheet limits, the marginal buyer is whoever can actually clear the trade — not whoever wants the yield.</li>
        </ol>

        <h3>[03] Call</h3>
        <p>
          If frame three is right, the next four weeks of auction tails are not a
          demand story. They're a plumbing story. The trade is not "short the long
          end" — it's <em>watch where the dealers stop bidding.</em>
        </p>

        <p>
          If I'm wrong, the primary sources are linked above — you can check.
        </p>
      </div>

      <hr className="tcn-hairline" />

      <Disclosure />
    </article>
  );
}

window.Dispatch = Dispatch;
window.Disclosure = Disclosure;
