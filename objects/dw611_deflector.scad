$fn = 40;
 union() {
     difference() {
         union() {
             translate([0.0, 0.0, 1.0]) {
                 render() {
                     difference() {
                         cylinder(r=20.75, h=9.0, center=true);
                         cylinder(r=13.0, h=10.8, center=true);
                    }

                }

            }

             difference() {
                 cylinder(r=37.5, h=11.0, center=true);
                 cylinder(r=20.75, h=13.0, center=true);
            }

        }

         translate([10.25, -25.3, 0.0]) {
             union() {
                 cylinder(r=2.35, h=13.0, center=true);
                 translate([0.0, 0.0, 3.45]) {
                     cylinder(r=3.5, h=4.1, center=true);
                }

            }

        }

         translate([-10.25, -25.3, 0.0]) {
             union() {
                 cylinder(r=2.35, h=13.0, center=true);
                 translate([0.0, 0.0, 3.45]) {
                     cylinder(r=3.5, h=4.1, center=true);
                }

            }

        }

         translate([26.0, 0.0, 0.0]) {
             cylinder(r1=4.25, r2=6.75, h=13.0, center=true);
        }

         translate([-26.0, 0.0, 0.0]) {
             cylinder(r1=4.25, r2=6.75, h=13.0, center=true);
        }

         translate([0.0, 0.0, -1.5]) {
             difference() {
                 render() {
                     difference() {
                         cylinder(r1=47.5, r2=20.75, h=8.05, center=true);
                         cylinder(r=21.75, h=9.66, center=true);
                    }

                }

                 cube([75.0, 13.5, 11.0], center=true);
                 translate([0.0, -18.0, -5.5]) {
                     linear_extrude(height=11.0, center=false, twist=0.0, slices=20, scale=1.0) {
                         polygon(points=[[-12.0, 0.0], [12.0, 0.0], [22.95, -20.0], [-22.95, -20.0]]);
                    }

                }

            }

        }

         union();
    }

     translate([10.25, -25.3, -6.7]) {
         render() {
             difference() {
                 cylinder(r=4.3815, h=2.4, center=true);
                 cylinder(r=2.35, h=2.4, center=true);
            }

        }

    }

     translate([-10.25, -25.3, -6.7]) {
         render() {
             difference() {
                 cylinder(r=4.3815, h=2.4, center=true);
                 cylinder(r=2.35, h=2.4, center=true);
            }

        }

    }

}
