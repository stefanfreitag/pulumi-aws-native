// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CleanRooms.Inputs
{

    public sealed class MembershipProtectedQueryOutputConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("s3", required: true)]
        public Input<Inputs.MembershipProtectedQueryS3OutputConfigurationArgs> S3 { get; set; } = null!;

        public MembershipProtectedQueryOutputConfigurationArgs()
        {
        }
        public static new MembershipProtectedQueryOutputConfigurationArgs Empty => new MembershipProtectedQueryOutputConfigurationArgs();
    }
}
