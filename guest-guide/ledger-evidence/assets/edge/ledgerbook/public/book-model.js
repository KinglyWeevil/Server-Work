(function(root){
  'use strict';
  const PAGE_SIZE=6;
  function openChapter(category,items){return {category,query:'',expanded:items.length>PAGE_SIZE,offset:0};}
  function goBack(state){return {...state,expanded:false,offset:0};}
  function expand(state){return {...state,expanded:true,offset:0};}
  function searchChapter(state,query,items){return {...state,query,offset:0,expanded:filter(items,query).length>PAGE_SIZE};}
  function filter(items,query){const q=query.trim().toLocaleLowerCase();return items.filter(s=>(s.name+' '+s.description).toLocaleLowerCase().includes(q));}
  function paginate(state,direction,count){const last=Math.max(0,Math.ceil(count/(PAGE_SIZE*2))-1)*PAGE_SIZE*2;return {...state,expanded:true,offset:Math.min(last,Math.max(0,state.offset+direction*PAGE_SIZE*2))};}
  function pages(state,items,pins){const list=filter(items,state.query);return {right:list.slice(state.offset,state.offset+PAGE_SIZE),left:state.expanded?list.slice(state.offset+PAGE_SIZE,state.offset+PAGE_SIZE*2):pins.slice(0,PAGE_SIZE),count:list.length,showBack:state.expanded,hasMore:list.length>PAGE_SIZE,hasNext:state.expanded&&state.offset+PAGE_SIZE*2<list.length,hasPrevious:state.expanded&&state.offset>0};}
  const model={PAGE_SIZE,openChapter,goBack,expand,searchChapter,filter,paginate,pages};
  root.BookModel=model;if(typeof module!=='undefined'&&module.exports)module.exports=model;
})(typeof globalThis!=='undefined'?globalThis:this);
