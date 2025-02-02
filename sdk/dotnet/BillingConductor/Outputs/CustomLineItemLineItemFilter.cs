// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.BillingConductor.Outputs
{

    [OutputType]
    public sealed class CustomLineItemLineItemFilter
    {
        public readonly Pulumi.AwsNative.BillingConductor.CustomLineItemLineItemFilterAttribute Attribute;
        public readonly Pulumi.AwsNative.BillingConductor.CustomLineItemLineItemFilterMatchOption MatchOption;
        public readonly ImmutableArray<Pulumi.AwsNative.BillingConductor.CustomLineItemLineItemFilterValue> Values;

        [OutputConstructor]
        private CustomLineItemLineItemFilter(
            Pulumi.AwsNative.BillingConductor.CustomLineItemLineItemFilterAttribute attribute,

            Pulumi.AwsNative.BillingConductor.CustomLineItemLineItemFilterMatchOption matchOption,

            ImmutableArray<Pulumi.AwsNative.BillingConductor.CustomLineItemLineItemFilterValue> values)
        {
            Attribute = attribute;
            MatchOption = matchOption;
            Values = values;
        }
    }
}
