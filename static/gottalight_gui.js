
document.getElementById("amount").value =1000;
document.getElementById("label").value = new Date().toLocaleString();
document.getElementById("desc").value = "generated by GottaLight";
document.getElementById("riskfactor").value =1;
document.getElementById("bolt11").value ="";

function getinfo(){
	window.location = "getinfo";
}
function listpeers(){
	window.location = "listpeers";
}
function listfunds(){
	window.location = "listfunds";
}
function listinvoices(){
	window.location = "listinvoices";
}

function pay(){
	var bolt11 = document.getElementById("bolt11");
	var bolt11_val = bolt11.value;
	$.get("pay?bolt11="+bolt11_val,
		function( data ) {
		  alert(data[1]+" "+data[0].message);
		}
	);
	//window.location = "pay?bolt11="+bolt11_val;
}

function delexpiredinvoice(){
	$.get("delexpiredinvoice",
		function( data ) {
		  alert(data[1]+" "+data[0].message);
		}
	);
}


function generateinvoice(){
	var amount = document.getElementById("amount");
	var label = document.getElementById("label");
	var desc = document.getElementById("desc");
	var amount_val = amount.value;
	var label_val = label.value;
	var desc_val = desc.value;

	/*
	$.get("invoice?amount="+amount_val+"&label="+label_val+"&desc="+desc_val,
		function( data ) {
			//var jsonPretty = JSON.stringify(JSON.parse(data[0]),null,2);  


		  //alert(data[1]+" "+data[0].message);
		}
	);
	*/
	window.location = "invoice?amount="+amount_val+"&label="+label_val+"&desc="+desc_val;

}
function generateinvoiceQR(){

	var amount = document.getElementById("amount");
	var label = document.getElementById("label");
	var desc = document.getElementById("desc");
	var amount_val = amount.value;
	var label_val = label.value;
	var desc_val = desc.value;

	/*
	$.get("invoiceqr?amount="+amount_val+"&label="+label_val+"&desc="+desc_val,
		function( data ) {
		  alert(data[1]+" "+data[0].message);
		}
	);

	if (data[1]=="SUCCESS")
		openQRDialog();
		*/

	window.location = "invoiceqr?amount="+amount_val+"&label="+label_val+"&desc="+desc_val;

}

function connect(){
	var id = document.getElementById("connect_node_id");
	var id_val = id.value;
	$.get("connect?id="+id_val,
		function( data ) {
		  alert(data[1]+" "+data[0].message);
		}
	);
	//window.location = "connect?id="+id_val;
}
function closeid(){
	var id = document.getElementById("close_node_id");
	var id_val = id.value;
	$.get("close?id="+id_val,
		function( data ) {
		  alert(data[1]+" "+data[0].message);
		}
	);
}
function disconnectid(){
	var id = document.getElementById("disconnect_node_id");
	var id_val = id.value;
	$.get("disconnect?id="+id_val,
		function( data ) {
		  alert(data[1]+" "+data[0].message);
		}
	);
	//window.location = "disconnect?id="+id_val;
}
function fundchannel(){
	var id = document.getElementById("fund_node_id");
	var id_val = id.value;
	var fund_amount = document.getElementById("fund_amount");
	var fund_amount_val = fund_amount.value;
	$.get("fundchannel?id="+id_val+"&amount="+fund_amount_val,
		function( data ) {
		  alert(data[1]+" "+data[0].message);
		}
	);
	//window.location = "fundchannel?id="+id_val+"&amount="+fund_amount_val;
}

function getroute(){
	var node_id = document.getElementById("node_id");
	var msatoshi = document.getElementById("msatoshi");
	var riskfactor = document.getElementById("riskfactor");
	var node_id_val = node_id.value;
	var msatoshi_val = msatoshi.value;
	var riskfactor_val = riskfactor.value;

	$.get("getroute?node_id="+node_id_val+"&msatoshi="+msatoshi_val+"&riskfactor="+riskfactor_val,
		function( data ) {
		  alert(data[1]+" "+data[0].message);
		}
	);

}

function getlog(){
	window.location = "getlog";
}
function listconfigs(){
	window.location = "listconfigs";
}
function listforwards(){
	window.location = "listforwards";
}
function devrescanoutputs(){
	window.location = "devrescanoutputs";
}

$( function() {
	$( "#dialog" ).dialog({
		autoOpen: false,
		show: {
			effect: "blind",
			duration: 1000
		},
		hide: {
			effect: "explode",
			duration: 1000
		}
	});

	$( "#test" ).on( "click", function() {
		$( "#dialog" ).dialog( "open" );
	});
} );

function openQRDialog(){

	$( "#dialog" ).dialog( "open" );
}
/*
$(function test() {
	$( "#dialog" ).dialog();
});
*/

