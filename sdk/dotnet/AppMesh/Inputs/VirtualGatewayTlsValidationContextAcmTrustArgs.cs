// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Inputs
{

    public sealed class VirtualGatewayTlsValidationContextAcmTrustArgs : global::Pulumi.ResourceArgs
    {
        [Input("certificateAuthorityArns", required: true)]
        private InputList<string>? _certificateAuthorityArns;
        public InputList<string> CertificateAuthorityArns
        {
            get => _certificateAuthorityArns ?? (_certificateAuthorityArns = new InputList<string>());
            set => _certificateAuthorityArns = value;
        }

        public VirtualGatewayTlsValidationContextAcmTrustArgs()
        {
        }
        public static new VirtualGatewayTlsValidationContextAcmTrustArgs Empty => new VirtualGatewayTlsValidationContextAcmTrustArgs();
    }
}
