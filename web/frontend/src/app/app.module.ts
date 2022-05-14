import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HeaderComponent } from './header/header';
import { LeftPanelComponent } from './left-panel/left-panel';
import { ProjectComponent } from './project/project';
import { TeamComponent } from './team/team';
import { AnalysisComponent } from './analysis/analysis';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule
  ],
  declarations: [
    AppComponent,
    DashboardComponent,
    HeaderComponent,
    LeftPanelComponent,
    ProjectComponent,
    TeamComponent,
    AnalysisComponent
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
