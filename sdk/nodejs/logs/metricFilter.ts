// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Specifies a metric filter that describes how CloudWatch Logs extracts information from logs and transforms it into Amazon CloudWatch metrics.
 */
export class MetricFilter extends pulumi.CustomResource {
    /**
     * Get an existing MetricFilter resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): MetricFilter {
        return new MetricFilter(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:logs:MetricFilter';

    /**
     * Returns true if the given object is an instance of MetricFilter.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MetricFilter {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MetricFilter.__pulumiType;
    }

    /**
     * A name for the metric filter.
     */
    public readonly filterName!: pulumi.Output<string | undefined>;
    /**
     * Pattern that Logs follows to interpret each entry in a log.
     */
    public readonly filterPattern!: pulumi.Output<string>;
    /**
     * Existing log group that you want to associate with this filter.
     */
    public readonly logGroupName!: pulumi.Output<string>;
    /**
     * A collection of information that defines how metric data gets emitted.
     */
    public readonly metricTransformations!: pulumi.Output<outputs.logs.MetricFilterMetricTransformation[]>;

    /**
     * Create a MetricFilter resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MetricFilterArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.filterPattern === undefined) && !opts.urn) {
                throw new Error("Missing required property 'filterPattern'");
            }
            if ((!args || args.logGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'logGroupName'");
            }
            if ((!args || args.metricTransformations === undefined) && !opts.urn) {
                throw new Error("Missing required property 'metricTransformations'");
            }
            resourceInputs["filterName"] = args ? args.filterName : undefined;
            resourceInputs["filterPattern"] = args ? args.filterPattern : undefined;
            resourceInputs["logGroupName"] = args ? args.logGroupName : undefined;
            resourceInputs["metricTransformations"] = args ? args.metricTransformations : undefined;
        } else {
            resourceInputs["filterName"] = undefined /*out*/;
            resourceInputs["filterPattern"] = undefined /*out*/;
            resourceInputs["logGroupName"] = undefined /*out*/;
            resourceInputs["metricTransformations"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["filterName", "logGroupName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(MetricFilter.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a MetricFilter resource.
 */
export interface MetricFilterArgs {
    /**
     * A name for the metric filter.
     */
    filterName?: pulumi.Input<string>;
    /**
     * Pattern that Logs follows to interpret each entry in a log.
     */
    filterPattern: pulumi.Input<string>;
    /**
     * Existing log group that you want to associate with this filter.
     */
    logGroupName: pulumi.Input<string>;
    /**
     * A collection of information that defines how metric data gets emitted.
     */
    metricTransformations: pulumi.Input<pulumi.Input<inputs.logs.MetricFilterMetricTransformationArgs>[]>;
}
