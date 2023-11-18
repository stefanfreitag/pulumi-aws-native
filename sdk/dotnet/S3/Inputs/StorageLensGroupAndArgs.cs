// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Inputs
{

    /// <summary>
    /// The Storage Lens group will include objects that match all of the specified filter values.
    /// </summary>
    public sealed class StorageLensGroupAndArgs : global::Pulumi.ResourceArgs
    {
        [Input("matchAnyPrefix")]
        private InputList<string>? _matchAnyPrefix;
        public InputList<string> MatchAnyPrefix
        {
            get => _matchAnyPrefix ?? (_matchAnyPrefix = new InputList<string>());
            set => _matchAnyPrefix = value;
        }

        [Input("matchAnySuffix")]
        private InputList<string>? _matchAnySuffix;
        public InputList<string> MatchAnySuffix
        {
            get => _matchAnySuffix ?? (_matchAnySuffix = new InputList<string>());
            set => _matchAnySuffix = value;
        }

        [Input("matchAnyTag")]
        private InputList<Inputs.StorageLensGroupTagArgs>? _matchAnyTag;
        public InputList<Inputs.StorageLensGroupTagArgs> MatchAnyTag
        {
            get => _matchAnyTag ?? (_matchAnyTag = new InputList<Inputs.StorageLensGroupTagArgs>());
            set => _matchAnyTag = value;
        }

        [Input("matchObjectAge")]
        public Input<Inputs.StorageLensGroupMatchObjectAgeArgs>? MatchObjectAge { get; set; }

        [Input("matchObjectSize")]
        public Input<Inputs.StorageLensGroupMatchObjectSizeArgs>? MatchObjectSize { get; set; }

        public StorageLensGroupAndArgs()
        {
        }
        public static new StorageLensGroupAndArgs Empty => new StorageLensGroupAndArgs();
    }
}
