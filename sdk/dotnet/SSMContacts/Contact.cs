// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SSMContacts
{
    /// <summary>
    /// Resource Type definition for AWS::SSMContacts::Contact
    /// </summary>
    [AwsNativeResourceType("aws-native:ssmcontacts:Contact")]
    public partial class Contact : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Alias of the contact. String value with 20 to 256 characters. Only alphabetical, numeric characters, dash, or underscore allowed.
        /// </summary>
        [Output("alias")]
        public Output<string> Alias { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the contact.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Name of the contact. String value with 3 to 256 characters. Only alphabetical, space, numeric characters, dash, or underscore allowed.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// The stages that an escalation plan or engagement plan engages contacts and contact methods in.
        /// </summary>
        [Output("plan")]
        public Output<ImmutableArray<Outputs.ContactStage>> Plan { get; private set; } = null!;

        /// <summary>
        /// Contact type, which specify type of contact. Currently supported values: “PERSONAL”, “SHARED”, “OTHER“.
        /// </summary>
        [Output("type")]
        public Output<Pulumi.AwsNative.SSMContacts.ContactType> Type { get; private set; } = null!;


        /// <summary>
        /// Create a Contact resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Contact(string name, ContactArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ssmcontacts:Contact", name, args ?? new ContactArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Contact(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ssmcontacts:Contact", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Contact resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Contact Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Contact(name, id, options);
        }
    }

    public sealed class ContactArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Alias of the contact. String value with 20 to 256 characters. Only alphabetical, numeric characters, dash, or underscore allowed.
        /// </summary>
        [Input("alias", required: true)]
        public Input<string> Alias { get; set; } = null!;

        /// <summary>
        /// Name of the contact. String value with 3 to 256 characters. Only alphabetical, space, numeric characters, dash, or underscore allowed.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        [Input("plan", required: true)]
        private InputList<Inputs.ContactStageArgs>? _plan;

        /// <summary>
        /// The stages that an escalation plan or engagement plan engages contacts and contact methods in.
        /// </summary>
        public InputList<Inputs.ContactStageArgs> Plan
        {
            get => _plan ?? (_plan = new InputList<Inputs.ContactStageArgs>());
            set => _plan = value;
        }

        /// <summary>
        /// Contact type, which specify type of contact. Currently supported values: “PERSONAL”, “SHARED”, “OTHER“.
        /// </summary>
        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.SSMContacts.ContactType> Type { get; set; } = null!;

        public ContactArgs()
        {
        }
        public static new ContactArgs Empty => new ContactArgs();
    }
}
