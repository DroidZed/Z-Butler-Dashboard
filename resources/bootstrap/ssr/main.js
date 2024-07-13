import { jsxs, Fragment, jsx } from "react/jsx-runtime";
import React from "react";
import ReactDOM from "react-dom/client";
import { createRootRoute, Outlet, createFileRoute, createRouter, RouterProvider } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/router-devtools";
const Route = createRootRoute({
  component: () => /* @__PURE__ */ jsxs(Fragment, { children: [
    /* @__PURE__ */ jsx(Outlet, {}),
    /* @__PURE__ */ jsx(TanStackRouterDevtools, {})
  ] })
});
const AboutLazyImport = createFileRoute("/about")();
const IndexLazyImport = createFileRoute("/")();
const AboutLazyRoute = AboutLazyImport.update({
  path: "/about",
  getParentRoute: () => Route
}).lazy(() => import("./assets/about.lazy-BFH7YIKU.js").then((d) => d.Route));
const IndexLazyRoute = IndexLazyImport.update({
  path: "/",
  getParentRoute: () => Route
}).lazy(() => import("./assets/index.lazy-B-mG5-2t.js").then((d) => d.Route));
const routeTree = Route.addChildren({
  IndexLazyRoute,
  AboutLazyRoute
});
const router = createRouter({ routeTree });
const rootElement = document.getElementById("app");
if (!rootElement.innerHTML) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    /* @__PURE__ */ jsx(React.StrictMode, { children: /* @__PURE__ */ jsx(RouterProvider, { router }) })
  );
}
