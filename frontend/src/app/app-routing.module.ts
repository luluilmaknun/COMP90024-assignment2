import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DashboardComponent } from './dashboard/dashboard.component';
import { ProjectComponent } from './project/project';
import { TeamComponent } from './team/team';
import { AnalysisComponent } from './analysis/analysis';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'project', component: ProjectComponent },
  { path: 'ourTeam', component: TeamComponent },
  { path: 'analysis', component: AnalysisComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
