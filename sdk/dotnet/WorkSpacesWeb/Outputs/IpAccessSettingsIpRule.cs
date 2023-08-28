// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WorkSpacesWeb.Outputs
{

    [OutputType]
    public sealed class IpAccessSettingsIpRule
    {
        public readonly string? Description;
        /// <summary>
        /// A single IP address or an IP address range in CIDR notation
        /// </summary>
        public readonly string IpRange;

        [OutputConstructor]
        private IpAccessSettingsIpRule(
            string? description,

            string ipRange)
        {
            Description = description;
            IpRange = ipRange;
        }
    }
}
