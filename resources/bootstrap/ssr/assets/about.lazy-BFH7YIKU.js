import { jsx } from "react/jsx-runtime";
import { M as MainLayout } from "./MainLayout-x8ZXAsW1.js";
import { createLazyFileRoute } from "@tanstack/react-router";
import "react-helmet-async";
const Route = createLazyFileRoute("/about")({
  component: About
});
function About() {
  return /* @__PURE__ */ jsx(
    MainLayout,
    {
      title: "About",
      description: "About page",
      keywords: "about, z butler",
      children: /* @__PURE__ */ jsx("div", { className: "p-2", children: "Hello from About!" })
    }
  );
}
export {
  Route
};
