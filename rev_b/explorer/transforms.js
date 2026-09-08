/* Pure, testable pose targets. Engineering mm -> scene coordinates explicitly 1:1. */
(function(root){
 const UNIT=1;
 function center(p){return p.bounds.min.map((v,k)=>(v+p.bounds.max[k])/2*UNIT)}
 const directions={Frame:[-1,0,-.3],Dosing:[-.75,0,1.1],Weighing:[0,-1,.4],Transfer:[0,-.7,-.4],Forming:[1,0,.7],Drives:[0,1,.6],Output:[1,-.3,-.5],Guarding:[0,-1.8,0],Electrical:[0,1.5,0]};
 function exploded(p,amount,scope,parts){const c=center(p);if(scope!=='all'&&scope!==p.assembly)return c;const siblings=parts.filter(q=>q.assembly===p.assembly);const n=siblings.findIndex(q=>q.id===p.id);const d=directions[p.assembly]||[1,0,1];return c.map((v,k)=>v+amount*(d[k]*270+(k===2?n*65:0)))}
 function grid(p,parts){const i=parts.findIndex(q=>q.id===p.id),cols=Math.ceil(Math.sqrt(parts.length));return [(i%cols-(cols-1)/2)*680,Math.floor(i/cols)*680,0]}
 const api={UNIT,center,exploded,grid};if(typeof module!=='undefined')module.exports=api;else root.POSES=api;
})(typeof window!=='undefined'?window:this);
