var tree = {}

$(function () {
    downloadContents(tree, '/', $('#browser'));    
});


function downloadContents(parentNode, node, domNode) {
    $.ajax({
        url: "/node-contents?node=" + node,
    }).done(function(data) {
        parentNode['node'] = node
        parentNode['children'] = data.children;

       domNode.append('<div>' + node + '</div>')
       var childDiv = document.createElement('div');
       for (i in parentNode['children']) {
            var nodeClass = 'file';
            console.log(parentNode['children'][i]['type']);
            if (parentNode['children'][i]['type'] == 'dir') {
                nodeClass = 'dir';
            }

            $(childDiv).append('<div data-node="' + node + '/' + parentNode['children'][i]['name'] + '" class="' + nodeClass + '">' + parentNode['children'][i]['name'] + '</div>');
       }
        
       domNode.append(childDiv);
       setupDirNodes();
    });    
}

function setupDirNodes() {
   $('.dir').click(function () {
        var curNode = $(this).data('node');
        downloadContents(tree, curNode, $(this));
   });    
}