// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DirectoryService
{
    /// <summary>
    /// Resource Type definition for AWS::DirectoryService::SimpleAD
    /// </summary>
    [Obsolete(@"SimpleAD is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:directoryservice:SimpleAD")]
    public partial class SimpleAD : global::Pulumi.CustomResource
    {
        [Output("alias")]
        public Output<string> Alias { get; private set; } = null!;

        [Output("createAlias")]
        public Output<bool?> CreateAlias { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("dnsIpAddresses")]
        public Output<ImmutableArray<string>> DnsIpAddresses { get; private set; } = null!;

        [Output("enableSso")]
        public Output<bool?> EnableSso { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        [Output("shortName")]
        public Output<string?> ShortName { get; private set; } = null!;

        [Output("size")]
        public Output<string> Size { get; private set; } = null!;

        [Output("vpcSettings")]
        public Output<Outputs.SimpleADVpcSettings> VpcSettings { get; private set; } = null!;


        /// <summary>
        /// Create a SimpleAD resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SimpleAD(string name, SimpleADArgs args, CustomResourceOptions? options = null)
            : base("aws-native:directoryservice:SimpleAD", name, args ?? new SimpleADArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SimpleAD(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:directoryservice:SimpleAD", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing SimpleAD resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SimpleAD Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SimpleAD(name, id, options);
        }
    }

    public sealed class SimpleADArgs : global::Pulumi.ResourceArgs
    {
        [Input("createAlias")]
        public Input<bool>? CreateAlias { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("enableSso")]
        public Input<bool>? EnableSso { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        [Input("shortName")]
        public Input<string>? ShortName { get; set; }

        [Input("size", required: true)]
        public Input<string> Size { get; set; } = null!;

        [Input("vpcSettings", required: true)]
        public Input<Inputs.SimpleADVpcSettingsArgs> VpcSettings { get; set; } = null!;

        public SimpleADArgs()
        {
        }
        public static new SimpleADArgs Empty => new SimpleADArgs();
    }
}
