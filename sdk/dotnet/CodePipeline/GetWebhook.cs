// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodePipeline
{
    public static class GetWebhook
    {
        /// <summary>
        /// Resource Type definition for AWS::CodePipeline::Webhook
        /// </summary>
        public static Task<GetWebhookResult> InvokeAsync(GetWebhookArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetWebhookResult>("aws-native:codepipeline:getWebhook", args ?? new GetWebhookArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::CodePipeline::Webhook
        /// </summary>
        public static Output<GetWebhookResult> Invoke(GetWebhookInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetWebhookResult>("aws-native:codepipeline:getWebhook", args ?? new GetWebhookInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetWebhookArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetWebhookArgs()
        {
        }
        public static new GetWebhookArgs Empty => new GetWebhookArgs();
    }

    public sealed class GetWebhookInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetWebhookInvokeArgs()
        {
        }
        public static new GetWebhookInvokeArgs Empty => new GetWebhookInvokeArgs();
    }


    [OutputType]
    public sealed class GetWebhookResult
    {
        public readonly string? Authentication;
        public readonly Outputs.WebhookAuthConfiguration? AuthenticationConfiguration;
        public readonly ImmutableArray<Outputs.WebhookFilterRule> Filters;
        public readonly string? Id;
        public readonly bool? RegisterWithThirdParty;
        public readonly string? TargetAction;
        public readonly string? TargetPipeline;
        public readonly int? TargetPipelineVersion;
        public readonly string? Url;

        [OutputConstructor]
        private GetWebhookResult(
            string? authentication,

            Outputs.WebhookAuthConfiguration? authenticationConfiguration,

            ImmutableArray<Outputs.WebhookFilterRule> filters,

            string? id,

            bool? registerWithThirdParty,

            string? targetAction,

            string? targetPipeline,

            int? targetPipelineVersion,

            string? url)
        {
            Authentication = authentication;
            AuthenticationConfiguration = authenticationConfiguration;
            Filters = filters;
            Id = id;
            RegisterWithThirdParty = registerWithThirdParty;
            TargetAction = targetAction;
            TargetPipeline = targetPipeline;
            TargetPipelineVersion = targetPipelineVersion;
            Url = url;
        }
    }
}
