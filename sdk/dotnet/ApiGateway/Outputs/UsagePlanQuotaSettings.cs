// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway.Outputs
{

    /// <summary>
    /// ``QuotaSettings`` is a property of the [AWS::ApiGateway::UsagePlan](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html) resource that specifies a target for the maximum number of requests users can make to your REST APIs.
    ///  In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using [](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor costs and [](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to manage API requests.
    /// </summary>
    [OutputType]
    public sealed class UsagePlanQuotaSettings
    {
        /// <summary>
        /// The target maximum number of requests that can be made in a given time period.
        /// </summary>
        public readonly int? Limit;
        /// <summary>
        /// The number of requests subtracted from the given limit in the initial time period.
        /// </summary>
        public readonly int? Offset;
        /// <summary>
        /// The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".
        /// </summary>
        public readonly string? Period;

        [OutputConstructor]
        private UsagePlanQuotaSettings(
            int? limit,

            int? offset,

            string? period)
        {
            Limit = limit;
            Offset = offset;
            Period = period;
        }
    }
}
