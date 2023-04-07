// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudTrail.Inputs
{

    /// <summary>
    /// A single selector statement in an advanced event selector.
    /// </summary>
    public sealed class EventDataStoreAdvancedFieldSelectorArgs : global::Pulumi.ResourceArgs
    {
        [Input("endsWith")]
        private InputList<string>? _endsWith;

        /// <summary>
        /// An operator that includes events that match the last few characters of the event record field specified as the value of Field.
        /// </summary>
        public InputList<string> EndsWith
        {
            get => _endsWith ?? (_endsWith = new InputList<string>());
            set => _endsWith = value;
        }

        [Input("equals")]
        private InputList<string>? _equals;

        /// <summary>
        /// An operator that includes events that match the exact value of the event record field specified as the value of Field. This is the only valid operator that you can use with the readOnly, eventCategory, and resources.type fields.
        /// </summary>
        public InputList<string> Equals
        {
            get => _equals ?? (_equals = new InputList<string>());
            set => _equals = value;
        }

        /// <summary>
        /// A field in an event record on which to filter events to be logged. Supported fields include readOnly, eventCategory, eventSource (for management events), eventName, resources.type, and resources.ARN.
        /// </summary>
        [Input("field", required: true)]
        public Input<string> Field { get; set; } = null!;

        [Input("notEndsWith")]
        private InputList<string>? _notEndsWith;

        /// <summary>
        /// An operator that excludes events that match the last few characters of the event record field specified as the value of Field.
        /// </summary>
        public InputList<string> NotEndsWith
        {
            get => _notEndsWith ?? (_notEndsWith = new InputList<string>());
            set => _notEndsWith = value;
        }

        [Input("notEquals")]
        private InputList<string>? _notEquals;

        /// <summary>
        /// An operator that excludes events that match the exact value of the event record field specified as the value of Field.
        /// </summary>
        public InputList<string> NotEquals
        {
            get => _notEquals ?? (_notEquals = new InputList<string>());
            set => _notEquals = value;
        }

        [Input("notStartsWith")]
        private InputList<string>? _notStartsWith;

        /// <summary>
        /// An operator that excludes events that match the first few characters of the event record field specified as the value of Field.
        /// </summary>
        public InputList<string> NotStartsWith
        {
            get => _notStartsWith ?? (_notStartsWith = new InputList<string>());
            set => _notStartsWith = value;
        }

        [Input("startsWith")]
        private InputList<string>? _startsWith;

        /// <summary>
        /// An operator that includes events that match the first few characters of the event record field specified as the value of Field.
        /// </summary>
        public InputList<string> StartsWith
        {
            get => _startsWith ?? (_startsWith = new InputList<string>());
            set => _startsWith = value;
        }

        public EventDataStoreAdvancedFieldSelectorArgs()
        {
        }
        public static new EventDataStoreAdvancedFieldSelectorArgs Empty => new EventDataStoreAdvancedFieldSelectorArgs();
    }
}
