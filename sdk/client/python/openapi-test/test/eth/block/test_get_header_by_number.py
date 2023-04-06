from base.testing import KlaytnBaseTesting


class TestEthGetHeaderByNumber(KlaytnBaseTesting):

    def setUp(self) -> None:
        super().setUp()
        self.blochTag = "0x1b4"

    def test_post(self):
        klay_response = self.sdk.eth.get_header_by_number(
            self.blochTag
        )

        self.covert_response(klay_response.response)
        self.assertResponseSuccess()
        self.assertIn("jsonrpc", self.response)
        self.assertIn("id", self.response)
        self.assertIn("result", self.response)

    def test_post_wrong_with_lack_paramaters(self):
        klay_response = self.sdk.eth.get_header_by_number()
        self.covert_response(klay_response.response)
        self.assertResponseSuccess()
        self.assertIn("jsonrpc", self.response)
        self.assertIn("id", self.response)
        self.assertIn("error", self.response)
        self.assertErrorCodeMissingRequiredArgument()