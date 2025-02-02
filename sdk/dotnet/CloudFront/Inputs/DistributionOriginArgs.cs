// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Inputs
{

    public sealed class DistributionOriginArgs : global::Pulumi.ResourceArgs
    {
        [Input("connectionAttempts")]
        public Input<int>? ConnectionAttempts { get; set; }

        [Input("connectionTimeout")]
        public Input<int>? ConnectionTimeout { get; set; }

        [Input("customOriginConfig")]
        public Input<Inputs.DistributionCustomOriginConfigArgs>? CustomOriginConfig { get; set; }

        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("originAccessControlId")]
        public Input<string>? OriginAccessControlId { get; set; }

        [Input("originCustomHeaders")]
        private InputList<Inputs.DistributionOriginCustomHeaderArgs>? _originCustomHeaders;
        public InputList<Inputs.DistributionOriginCustomHeaderArgs> OriginCustomHeaders
        {
            get => _originCustomHeaders ?? (_originCustomHeaders = new InputList<Inputs.DistributionOriginCustomHeaderArgs>());
            set => _originCustomHeaders = value;
        }

        [Input("originPath")]
        public Input<string>? OriginPath { get; set; }

        [Input("originShield")]
        public Input<Inputs.DistributionOriginShieldArgs>? OriginShield { get; set; }

        [Input("s3OriginConfig")]
        public Input<Inputs.DistributionS3OriginConfigArgs>? S3OriginConfig { get; set; }

        public DistributionOriginArgs()
        {
        }
        public static new DistributionOriginArgs Empty => new DistributionOriginArgs();
    }
}
