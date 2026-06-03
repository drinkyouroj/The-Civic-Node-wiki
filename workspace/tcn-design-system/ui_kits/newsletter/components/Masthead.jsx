// Masthead.jsx — The Civic Node
// Mark + wordmark + nav + standing-furniture row.

const TCNMark = ({ size = 28, color = "#557fa3" }) => (
  <svg width={size} height={size * 1.08} viewBox="-3 -3 120 130" fill="none"
       stroke={color} strokeWidth="6" strokeLinecap="round">
    <line x1="33" y1="0" x2="81" y2="0"/>
    <line x1="57" y1="0" x2="57" y2="77"/>
    <line x1="57" y1="77" x2="0" y2="110"/>
    <line x1="57" y1="77" x2="114" y2="110"/>
    <circle cx="57" cy="77" r="14" fill={color} stroke="none"/>
  </svg>
);

const NAV = [
  { label: "Home",      href: "#home",     active: true  },
  { label: "Archive",   href: "#archive"                  },
  { label: "About",     href: "#about"                    },
  { label: "Subscribe →", href: "#subscribe", primary: true },
];

function Masthead({ activeNav = "Home", onNav = () => {} }) {
  return (
    <header className="tcn-masthead">
      <div className="tcn-masthead-row">
        <a className="tcn-mast-brand" href="#home" onClick={(e) => { e.preventDefault(); onNav("Home"); }}>
          <TCNMark size={26} />
          <span className="tcn-mast-word">The Civic Node</span>
        </a>
        <nav className="tcn-mast-nav">
          {NAV.map(n => (
            <a key={n.label}
               href={n.href}
               className={[
                 "tcn-mast-link",
                 (n.label === activeNav) ? "is-active" : "",
                 n.primary ? "is-primary" : "",
               ].join(" ")}
               onClick={(e) => { e.preventDefault(); onNav(n.label); }}>
              {n.label}
            </a>
          ))}
        </nav>
      </div>
      <div className="tcn-mast-furniture">
        <span>EST. 2025</span>
        <span aria-hidden>·</span>
        <span>DRINKYOUROJ.SUBSTACK.COM</span>
        <span aria-hidden>·</span>
        <span>DISPATCHES FROM INSIDE THE MACHINE</span>
      </div>
      <hr className="tcn-hairline" />
    </header>
  );
}

window.Masthead = Masthead;
window.TCNMark = TCNMark;
