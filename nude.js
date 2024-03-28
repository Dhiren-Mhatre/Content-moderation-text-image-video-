nude.load(node);
// Scan it
nude.scan(function(result){ 
    alert(result ? "Nudity found in " + node.id + "!" : "Not nude");
});