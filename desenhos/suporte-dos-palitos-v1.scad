// height 2m in H0 scale
// diameter 80cm in H0 scale

$fn=30;

difference(){
    cylinder(d=9.1954,h=22.98);
    translate([0,0,-0.1])
    cylinder(d=8.2,h=5.1);
    translate([0,0,6.5])
    cylinder(d=4.9,h=22.9885);
}