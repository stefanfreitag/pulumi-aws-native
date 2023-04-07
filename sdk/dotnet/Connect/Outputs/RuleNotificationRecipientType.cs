// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Outputs
{

    /// <summary>
    /// The type of notification recipient.
    /// </summary>
    [OutputType]
    public sealed class RuleNotificationRecipientType
    {
        /// <summary>
        /// The list of recipients by user arns.
        /// </summary>
        public readonly ImmutableArray<string> UserArns;
        /// <summary>
        /// The collection of recipients who are identified by user tags
        /// </summary>
        public readonly object? UserTags;

        [OutputConstructor]
        private RuleNotificationRecipientType(
            ImmutableArray<string> userArns,

            object? userTags)
        {
            UserArns = userArns;
            UserTags = userTags;
        }
    }
}
