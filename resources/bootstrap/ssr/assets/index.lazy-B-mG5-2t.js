import { jsx } from "react/jsx-runtime";
import { M as MainLayout } from "./MainLayout-x8ZXAsW1.js";
import { createLazyFileRoute } from "@tanstack/react-router";
import "react-helmet-async";
const Route = createLazyFileRoute("/")({
  component: Index
});
function Index() {
  return /* @__PURE__ */ jsx(MainLayout, { title: "Home", description: "Home page", keywords: "home, z butler", children: /* @__PURE__ */ jsx("div", { className: "p-2", children: /* @__PURE__ */ jsx("h3", { children: "Welcome Home!" }) }) });
}
export {
  Route
};
