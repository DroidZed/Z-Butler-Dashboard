import { jsx } from "react/jsx-runtime";
import React from "react";
import ReactDOM from "react-dom/client";
import { createRouter, RouterProvider } from "@tanstack/react-router";
import { routeTree } from "routeTree.gen";
const router = createRouter({ routeTree });
const rootElement = document.getElementById("app");
if (!rootElement.innerHTML) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    /* @__PURE__ */ jsx(React.StrictMode, { children: /* @__PURE__ */ jsx(RouterProvider, { router }) })
  );
}
