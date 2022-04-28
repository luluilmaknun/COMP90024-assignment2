import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Analysis } from './analysis.model';

@Injectable({
  providedIn: 'root'
})
export class AnalysisService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse) {
    return throwError(() => err.message || 'Error: Unable to complete request.');
  }

  // GET list of analysis
  public getAnalysis() {
    return this.http
      .get<Analysis[]>(`api/analysis`)
      .pipe(catchError(AnalysisService._handleError));
  }
}
