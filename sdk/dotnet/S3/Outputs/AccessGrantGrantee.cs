// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Outputs
{

    [OutputType]
    public sealed class AccessGrantGrantee
    {
        /// <summary>
        /// The unique identifier of the Grantee
        /// </summary>
        public readonly string GranteeIdentifier;
        /// <summary>
        /// Configures the transfer acceleration state for an Amazon S3 bucket.
        /// </summary>
        public readonly Pulumi.AwsNative.S3.AccessGrantGranteeGranteeType GranteeType;

        [OutputConstructor]
        private AccessGrantGrantee(
            string granteeIdentifier,

            Pulumi.AwsNative.S3.AccessGrantGranteeGranteeType granteeType)
        {
            GranteeIdentifier = granteeIdentifier;
            GranteeType = granteeType;
        }
    }
}
