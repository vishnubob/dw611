 difference() {
     difference() {
         difference() {
             hull() {
                 cylinder(r=37.5, h=5.5, center=true);
                 translate([70.875, 0.0, 0.0]) {
                     cylinder(r=27.875, h=5.5, center=true);
                }

            }

             hull() {
                 cylinder(r=24.375, h=6.5, center=true);
                 translate([70.875, 0.0, 0.0]) {
                     cylinder(r=16.725, h=6.5, center=true);
                }

            }

        }

         union() {
             translate([70.875, 21.6, 0.0]) {
                 translate([0.0, 0.0, 2.05625]) {
                     cylinder(r=3.275, h=1.5875, center=true);
                }

            }

             translate([70.875, -21.6, 0.0]) {
                 translate([0.0, 0.0, 2.05625]) {
                     cylinder(r=3.275, h=1.5875, center=true);
                }

            }

             translate([0.0, 31.225, 0.0]) {
                 translate([0.0, 0.0, 2.05625]) {
                     cylinder(r=3.275, h=1.5875, center=true);
                }

            }

             translate([0.0, -31.225, 0.0]) {
                 translate([0.0, 0.0, 2.05625]) {
                     cylinder(r=3.275, h=1.5875, center=true);
                }

            }

        }

    }

     translate([0.0, 0.0, -2.75]) {
         difference() {
             hull() {
                 cylinder(r=33.0, h=5.5, center=true);
                 translate([70.875, 0.0, 0.0]) {
                     cylinder(r=24.53, h=6.5, center=true);
                }

            }

             hull() {
                 cylinder(r=29.25, h=7.5, center=true);
                 translate([70.875, 0.0, 0.0]) {
                     cylinder(r=20.78, h=7.5, center=true);
                }

            }

        }

    }

}
