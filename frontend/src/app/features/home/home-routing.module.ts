import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeOverviewComponent } from './pages/home-overview/home-overview.component';
import { HomeRoomOverviewComponent } from './pages/home-room-overview/home-room-overview.component';

import { AuthGuard } from '../../core/auth/auth.guard';

/*
To add child routes of a parent path:
{ path: ParentPath, component: ParentComponent, children: [
  { path: ChildPath1, component: ChildComponent1 },
  { path: ChildPath2, component: ChildComponent2 }
] }
To add guards:
{ path: Path, component: Component, canActivate: [<Guard>, <Guard>, ...] }
Or for all children:
{ path: Path, component: Component, canActivateChild: [<Guard>, <Guard>, ...] }
NOTE! canDeactivate can be used to prevent navigation before saving changes.
 */

const routes: Routes = [
  { path: 'home',
    component: HomeOverviewComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'home/:id',
    component: HomeRoomOverviewComponent,
    canActivate: [AuthGuard]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomeRoutingModule {}
