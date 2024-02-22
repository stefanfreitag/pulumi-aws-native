// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CustomerProfiles
{
    public static class GetCalculatedAttributeDefinition
    {
        /// <summary>
        /// A calculated attribute definition for Customer Profiles
        /// </summary>
        public static Task<GetCalculatedAttributeDefinitionResult> InvokeAsync(GetCalculatedAttributeDefinitionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCalculatedAttributeDefinitionResult>("aws-native:customerprofiles:getCalculatedAttributeDefinition", args ?? new GetCalculatedAttributeDefinitionArgs(), options.WithDefaults());

        /// <summary>
        /// A calculated attribute definition for Customer Profiles
        /// </summary>
        public static Output<GetCalculatedAttributeDefinitionResult> Invoke(GetCalculatedAttributeDefinitionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCalculatedAttributeDefinitionResult>("aws-native:customerprofiles:getCalculatedAttributeDefinition", args ?? new GetCalculatedAttributeDefinitionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCalculatedAttributeDefinitionArgs : global::Pulumi.InvokeArgs
    {
        [Input("calculatedAttributeName", required: true)]
        public string CalculatedAttributeName { get; set; } = null!;

        [Input("domainName", required: true)]
        public string DomainName { get; set; } = null!;

        public GetCalculatedAttributeDefinitionArgs()
        {
        }
        public static new GetCalculatedAttributeDefinitionArgs Empty => new GetCalculatedAttributeDefinitionArgs();
    }

    public sealed class GetCalculatedAttributeDefinitionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("calculatedAttributeName", required: true)]
        public Input<string> CalculatedAttributeName { get; set; } = null!;

        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        public GetCalculatedAttributeDefinitionInvokeArgs()
        {
        }
        public static new GetCalculatedAttributeDefinitionInvokeArgs Empty => new GetCalculatedAttributeDefinitionInvokeArgs();
    }


    [OutputType]
    public sealed class GetCalculatedAttributeDefinitionResult
    {
        public readonly Outputs.CalculatedAttributeDefinitionAttributeDetails? AttributeDetails;
        public readonly Outputs.CalculatedAttributeDefinitionConditions? Conditions;
        /// <summary>
        /// The timestamp of when the calculated attribute definition was created.
        /// </summary>
        public readonly string? CreatedAt;
        public readonly string? Description;
        public readonly string? DisplayName;
        /// <summary>
        /// The timestamp of when the calculated attribute definition was most recently edited.
        /// </summary>
        public readonly string? LastUpdatedAt;
        public readonly Pulumi.AwsNative.CustomerProfiles.CalculatedAttributeDefinitionStatistic? Statistic;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetCalculatedAttributeDefinitionResult(
            Outputs.CalculatedAttributeDefinitionAttributeDetails? attributeDetails,

            Outputs.CalculatedAttributeDefinitionConditions? conditions,

            string? createdAt,

            string? description,

            string? displayName,

            string? lastUpdatedAt,

            Pulumi.AwsNative.CustomerProfiles.CalculatedAttributeDefinitionStatistic? statistic,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            AttributeDetails = attributeDetails;
            Conditions = conditions;
            CreatedAt = createdAt;
            Description = description;
            DisplayName = displayName;
            LastUpdatedAt = lastUpdatedAt;
            Statistic = statistic;
            Tags = tags;
        }
    }
}
