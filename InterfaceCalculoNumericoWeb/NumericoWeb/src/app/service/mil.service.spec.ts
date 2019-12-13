import { TestBed } from '@angular/core/testing';

import { MilService } from './mil.service';

describe('MilService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: MilService = TestBed.get(MilService);
    expect(service).toBeTruthy();
  });
});
