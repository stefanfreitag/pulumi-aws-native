// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Route53Resolver
{
    public static class GetResolverRule
    {
        /// <summary>
        /// Resource Type definition for AWS::Route53Resolver::ResolverRule
        /// </summary>
        public static Task<GetResolverRuleResult> InvokeAsync(GetResolverRuleArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetResolverRuleResult>("aws-native:route53resolver:getResolverRule", args ?? new GetResolverRuleArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Route53Resolver::ResolverRule
        /// </summary>
        public static Output<GetResolverRuleResult> Invoke(GetResolverRuleInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetResolverRuleResult>("aws-native:route53resolver:getResolverRule", args ?? new GetResolverRuleInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetResolverRuleArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the endpoint that the rule is associated with.
        /// </summary>
        [Input("resolverRuleId", required: true)]
        public string ResolverRuleId { get; set; } = null!;

        public GetResolverRuleArgs()
        {
        }
        public static new GetResolverRuleArgs Empty => new GetResolverRuleArgs();
    }

    public sealed class GetResolverRuleInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the endpoint that the rule is associated with.
        /// </summary>
        [Input("resolverRuleId", required: true)]
        public Input<string> ResolverRuleId { get; set; } = null!;

        public GetResolverRuleInvokeArgs()
        {
        }
        public static new GetResolverRuleInvokeArgs Empty => new GetResolverRuleInvokeArgs();
    }


    [OutputType]
    public sealed class GetResolverRuleResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the resolver rule.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The name for the Resolver rule
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The ID of the endpoint that the rule is associated with.
        /// </summary>
        public readonly string? ResolverEndpointId;
        /// <summary>
        /// The ID of the endpoint that the rule is associated with.
        /// </summary>
        public readonly string? ResolverRuleId;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.ResolverRuleTag> Tags;
        /// <summary>
        /// An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network. Specify IPv4 addresses. IPv6 is not supported.
        /// </summary>
        public readonly ImmutableArray<Outputs.ResolverRuleTargetAddress> TargetIps;

        [OutputConstructor]
        private GetResolverRuleResult(
            string? arn,

            string? name,

            string? resolverEndpointId,

            string? resolverRuleId,

            ImmutableArray<Outputs.ResolverRuleTag> tags,

            ImmutableArray<Outputs.ResolverRuleTargetAddress> targetIps)
        {
            Arn = arn;
            Name = name;
            ResolverEndpointId = resolverEndpointId;
            ResolverRuleId = resolverRuleId;
            Tags = tags;
            TargetIps = targetIps;
        }
    }
}
