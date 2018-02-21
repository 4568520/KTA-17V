<?php
require_once("TCPDF/tcpdf.php");

$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$pdf->AddPage();
$pdf->SetXY(20,50);
$pdf->SetFont('times', 'BI', 8);
$products=Array();
$products[0]=Array();
$products[0]['code']='item16';
$products[0]['name']='shoose';
$products[0]['count']='12';
$products[0]['price']='8';
$products[1]=Array();
$products[1]['code']='item02';
$products[1]['name']='Plate';
$products[1]['count']='3';
$products[1]['price']='1.5';
$products[2]=Array();
$products[2]['code']='item165';
$products[2]['name']='Shelf';
$products[2]['count']='1';
$products[2]['price']='20';
$summ=0;
$htmlText='<table border="1">';
foreach($products as $prodKey => $prodValue){
	$htmlText.='<tr><td>'.$prodValue['code'].'</td>';
	$htmlText.='<td>'.$prodValue['name'].'</td>';
	$htmlText.='<td>'.$prodValue['count'].'</td>';
	$htmlText.='<td>'.$prodValue['price'].'</td>';
	$htmlText.='<td>'.((float)$prodValue['price']*(float)$prodValue['count']).'</td>';
	$htmlText.='<td>'.((float)$prodValue['price']*(float)$prodValue['count']*0.2).'</td></tr>';
	$summ+=(float)$prodValue['price']*(float)$prodValue['count'];
}
$htmlText.='</table>';
$pdf->writeHTML($htmlText, true, false, true, false, '');
$pdf->Cell(0, 0, 'Total:'.$summ, 1, 1, 'C', 0, '', 0);


$pdf->Output('example_004.pdf', 'I');
?>