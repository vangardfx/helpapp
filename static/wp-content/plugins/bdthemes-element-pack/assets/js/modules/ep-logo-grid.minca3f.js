!function(t,n){"use strict";var e=function(t,n){var e=t.find(".bdt-logo-grid-wrapper");if(e.length){var o=e.find("> .bdt-tippy-tooltip"),i=t.data("id");o.each((function(t){tippy(this,{allowHTML:!0,theme:"bdt-tippy-"+i})}))}};jQuery(window).on("elementor/frontend/init",(function(){elementorFrontend.hooks.addAction("frontend/element_ready/bdt-logo-grid.default",e)}))}(jQuery,window.elementorFrontend);