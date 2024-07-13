import { jsxs, jsx } from "react/jsx-runtime";
import { HelmetProvider, Helmet } from "react-helmet-async";
import { Link } from "@tanstack/react-router";
const favicon = "/static/assets/favicon-DgzGEkrE.png";
const helmetContext = {};
const MainLayout = ({
  children,
  title,
  description,
  keywords
}) => {
  return /* @__PURE__ */ jsxs(HelmetProvider, { context: helmetContext, children: [
    /* @__PURE__ */ jsxs(Helmet, { children: [
      /* @__PURE__ */ jsx("meta", { charSet: "utf-8" }),
      /* @__PURE__ */ jsx("link", { rel: "icon", type: "image/x-icon", href: favicon }),
      /* @__PURE__ */ jsx("meta", { name: "description", content: description }),
      /* @__PURE__ */ jsx("meta", { name: "keywords", content: keywords }),
      /* @__PURE__ */ jsxs("title", { children: [
        "Z - Dashboard - ",
        title
      ] })
    ] }),
    /* @__PURE__ */ jsxs("div", { className: "p-2 flex gap-2", children: [
      /* @__PURE__ */ jsx(Link, { to: "/", className: "[&.active]:font-bold", children: "Home" }),
      " ",
      /* @__PURE__ */ jsx(Link, { to: "/about", className: "[&.active]:font-bold", children: "About" })
    ] }),
    /* @__PURE__ */ jsx("hr", {}),
    /* @__PURE__ */ jsx("main", { children })
  ] });
};
export {
  MainLayout as M
};
