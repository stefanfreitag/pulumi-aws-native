// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Route53Resolver
{
    /// <summary>
    /// Resource schema for AWS::Route53Resolver::ResolverDNSSECConfig.
    /// </summary>
    [AwsNativeResourceType("aws-native:route53resolver:ResolverDNSSECConfig")]
    public partial class ResolverDNSSECConfig : global::Pulumi.CustomResource
    {
        /// <summary>
        /// AccountId
        /// </summary>
        [Output("ownerId")]
        public Output<string> OwnerId { get; private set; } = null!;

        /// <summary>
        /// ResourceId
        /// </summary>
        [Output("resourceId")]
        public Output<string?> ResourceId { get; private set; } = null!;

        /// <summary>
        /// ResolverDNSSECValidationStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
        /// </summary>
        [Output("validationStatus")]
        public Output<Pulumi.AwsNative.Route53Resolver.ResolverDNSSECConfigValidationStatus> ValidationStatus { get; private set; } = null!;


        /// <summary>
        /// Create a ResolverDNSSECConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ResolverDNSSECConfig(string name, ResolverDNSSECConfigArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:route53resolver:ResolverDNSSECConfig", name, args ?? new ResolverDNSSECConfigArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ResolverDNSSECConfig(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:route53resolver:ResolverDNSSECConfig", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ResolverDNSSECConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ResolverDNSSECConfig Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ResolverDNSSECConfig(name, id, options);
        }
    }

    public sealed class ResolverDNSSECConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// ResourceId
        /// </summary>
        [Input("resourceId")]
        public Input<string>? ResourceId { get; set; }

        public ResolverDNSSECConfigArgs()
        {
        }
        public static new ResolverDNSSECConfigArgs Empty => new ResolverDNSSECConfigArgs();
    }
}
