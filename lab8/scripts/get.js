import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: Number(__ENV.VUS || 10),
  duration: __ENV.DURATION || '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<800'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://test.k6.io';
const PATH = __ENV.PATH || '/';

export default function () {
  const res = http.get(`${BASE_URL}${PATH}`, { tags: { endpoint: 'GET_root' } });

  check(res, {
    'status is 2xx': (r) => r.status >= 200 && r.status < 300,
    'has body': (r) => (r.body || '').length > 0,
  });

  sleep(Number(__ENV.SLEEP || 1));
}
