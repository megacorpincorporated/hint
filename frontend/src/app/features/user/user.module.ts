import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

// COMPONENTS

// PAGES
import { UserOverviewComponent } from './pages/user-overview/user-overview.component';

// SERVICES
import { UserService } from './user.service';

// MODULES
import { UserRoutingModule } from './user-routing.module';

@NgModule({
  declarations: [
    UserOverviewComponent
  ],
  imports: [
    UserRoutingModule,
    CommonModule
  ],
  exports: [

  ],
  providers: []
})
export class UserModule {}
