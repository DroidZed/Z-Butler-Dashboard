const __vite__mapDeps=(i,m=__vite__mapDeps,d=(m.f||(m.f=["assets/about.lazy-UbBwS9ve.js","assets/vendor-BysuFcG7.js","assets/MainLayout-B7ry4EB3.js","assets/index.lazy-7KsPB8M1.js"])))=>i.map(i=>d[i]);
import{c as E,j as c,O as L,T as v,a as p,b as P,d as b,R as _,e as O}from"./vendor-BysuFcG7.js";(function(){const i=document.createElement("link").relList;if(i&&i.supports&&i.supports("modulepreload"))return;for(const t of document.querySelectorAll('link[rel="modulepreload"]'))l(t);new MutationObserver(t=>{for(const e of t)if(e.type==="childList")for(const r of e.addedNodes)r.tagName==="LINK"&&r.rel==="modulepreload"&&l(r)}).observe(document,{childList:!0,subtree:!0});function a(t){const e={};return t.integrity&&(e.integrity=t.integrity),t.referrerPolicy&&(e.referrerPolicy=t.referrerPolicy),t.crossOrigin==="use-credentials"?e.credentials="include":t.crossOrigin==="anonymous"?e.credentials="omit":e.credentials="same-origin",e}function l(t){if(t.ep)return;t.ep=!0;const e=a(t);fetch(t.href,e)}})();const x="modulepreload",I=function(o){return"/static/"+o},f={},h=function(i,a,l){let t=Promise.resolve();if(a&&a.length>0){document.getElementsByTagName("link");const e=document.querySelector("meta[property=csp-nonce]"),r=(e==null?void 0:e.nonce)||(e==null?void 0:e.getAttribute("nonce"));t=Promise.all(a.map(n=>{if(n=I(n),n in f)return;f[n]=!0;const u=n.endsWith(".css"),y=u?'[rel="stylesheet"]':"";if(document.querySelector(`link[href="${n}"]${y}`))return;const s=document.createElement("link");if(s.rel=u?"stylesheet":x,u||(s.as="script",s.crossOrigin=""),s.href=n,r&&s.setAttribute("nonce",r),document.head.appendChild(s),u)return new Promise((R,g)=>{s.addEventListener("load",R),s.addEventListener("error",()=>g(new Error(`Unable to preload CSS for ${n}`)))})}))}return t.then(()=>i()).catch(e=>{const r=new Event("vite:preloadError",{cancelable:!0});if(r.payload=e,window.dispatchEvent(r),!r.defaultPrevented)throw e})},d=E({component:()=>c.jsxs(c.Fragment,{children:[c.jsx(L,{}),c.jsx(v,{})]})}),S=p("/about")(),j=p("/")(),w=S.update({path:"/about",getParentRoute:()=>d}).lazy(()=>h(()=>import("./about.lazy-UbBwS9ve.js"),__vite__mapDeps([0,1,2])).then(o=>o.Route)),A=j.update({path:"/",getParentRoute:()=>d}).lazy(()=>h(()=>import("./index.lazy-7KsPB8M1.js"),__vite__mapDeps([3,1,2])).then(o=>o.Route)),T=d.addChildren({IndexLazyRoute:A,AboutLazyRoute:w}),z=P({routeTree:T}),m=document.getElementById("app");m.innerHTML||b.createRoot(m).render(c.jsx(_.StrictMode,{children:c.jsx(O,{router:z})}));
