// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice
{
    /// <summary>
    /// Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services.
    /// </summary>
    [AwsNativeResourceType("aws-native:vpclattice:Listener")]
    public partial class Listener : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("defaultAction")]
        public Output<Outputs.ListenerDefaultAction> DefaultAction { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("port")]
        public Output<int?> Port { get; private set; } = null!;

        [Output("protocol")]
        public Output<Pulumi.AwsNative.VpcLattice.ListenerProtocol> Protocol { get; private set; } = null!;

        [Output("serviceArn")]
        public Output<string> ServiceArn { get; private set; } = null!;

        [Output("serviceId")]
        public Output<string> ServiceId { get; private set; } = null!;

        [Output("serviceIdentifier")]
        public Output<string?> ServiceIdentifier { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.ListenerTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Listener resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Listener(string name, ListenerArgs args, CustomResourceOptions? options = null)
            : base("aws-native:vpclattice:Listener", name, args ?? new ListenerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Listener(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:vpclattice:Listener", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Listener resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Listener Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Listener(name, id, options);
        }
    }

    public sealed class ListenerArgs : global::Pulumi.ResourceArgs
    {
        [Input("defaultAction", required: true)]
        public Input<Inputs.ListenerDefaultActionArgs> DefaultAction { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("protocol", required: true)]
        public Input<Pulumi.AwsNative.VpcLattice.ListenerProtocol> Protocol { get; set; } = null!;

        [Input("serviceIdentifier")]
        public Input<string>? ServiceIdentifier { get; set; }

        [Input("tags")]
        private InputList<Inputs.ListenerTagArgs>? _tags;
        public InputList<Inputs.ListenerTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ListenerTagArgs>());
            set => _tags = value;
        }

        public ListenerArgs()
        {
        }
        public static new ListenerArgs Empty => new ListenerArgs();
    }
}
