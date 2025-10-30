import http from 'k6/http';
import { check } from 'k6';

const BASE_URL = __ENV.BASE_URL || 'https://test.k6.io';
const PATH = __ENV.PATH || '/';

export const options = {
  scenarios: {
    constant_load: {
      executor: 'constant-vus',
      vus: Number(__ENV.VUS1 || 10),
      duration: __ENV.DUR1 || '30s',
      exec: 'call',
      tags: { scenario: 'constant' },
    },
    spike_load: {
      executor: 'constant-vus',
      vus: Number(__ENV.VUS2 || 50),
      duration: __ENV.DUR2 || '10s',
      exec: 'call',
      startTime: __ENV.START2 || '31s',
      tags: { scenario: 'spike' },
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<1000'],
  },
};

export function call() {
  const res = http.get(`${BASE_URL}${PATH}`);
  check(res, {
    'status is 2xx': (r) => r.status >= 200 && r.status < 300,
  });
}
