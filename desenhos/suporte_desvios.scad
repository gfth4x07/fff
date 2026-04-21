cube_l=35+2;
cube_w = 7;

mola_r = 5;
mola_l =35;

inner_cube_l=11;
inner_cube_w=4;

//mola_l_max=30;

$fn =20;
difference(){
translate([cube_l/2,0,cube_w/2])cube([cube_l,cube_w,cube_w],center=true);

    translate([0,0,mola_r/2])
    rotate([0,90,0])
    #cylinder(d=mola_r,h=mola_l);
    
    #translate([inner_cube_l/2,0,inner_cube_w/2])
    cube([inner_cube_l,inner_cube_w,inner_cube_w],center=true);
}