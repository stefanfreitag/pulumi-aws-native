// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElastiCache
{
    /// <summary>
    /// Resource Type definition for AWS::ElastiCache::ParameterGroup
    /// </summary>
    [Obsolete(@"ParameterGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:elasticache:ParameterGroup")]
    public partial class ParameterGroup : global::Pulumi.CustomResource
    {
        [Output("cacheParameterGroupFamily")]
        public Output<string> CacheParameterGroupFamily { get; private set; } = null!;

        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        [Output("properties")]
        public Output<ImmutableDictionary<string, string>?> Properties { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ParameterGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ParameterGroup(string name, ParameterGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:elasticache:ParameterGroup", name, args ?? new ParameterGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ParameterGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:elasticache:ParameterGroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "cacheParameterGroupFamily",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ParameterGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ParameterGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ParameterGroup(name, id, options);
        }
    }

    public sealed class ParameterGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("cacheParameterGroupFamily", required: true)]
        public Input<string> CacheParameterGroupFamily { get; set; } = null!;

        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        [Input("properties")]
        private InputMap<string>? _properties;
        public InputMap<string> Properties
        {
            get => _properties ?? (_properties = new InputMap<string>());
            set => _properties = value;
        }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public ParameterGroupArgs()
        {
        }
        public static new ParameterGroupArgs Empty => new ParameterGroupArgs();
    }
}
